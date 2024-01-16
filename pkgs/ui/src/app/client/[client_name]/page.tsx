"use client";
import { useEffect, useMemo, useRef, useState } from "react";
import { ClientTableConfig, ServiceTableConfig } from "@/config/client_1";
import CustomTable from "@/components/table";
import {
  Alert,
  Button,
  Card,
  CardContent,
  CardHeader,
  Snackbar,
  Typography,
  CircularProgress,
  IconButton,
} from "@mui/material";
import CopyToClipboard from "@/components/copy_to_clipboard";
import {
  attachEntity,
  detachEntity,
  isAttached,
} from "@/api/entities/entities";
import { mutate } from "swr";
import { Skeleton } from "@mui/material";
import { Entity, Service } from "@/api/model";
import useGetEntityByNameOrDid from "@/components/hooks/useGetEntityByNameOrDid";
import { useGetAllServices } from "@/api/services/services";
import axios from "axios";
import CloseIcon from "@mui/icons-material/Close";

interface SnackMessage {
  message: string;
  severity: "success" | "error";
}

type AttachButtonProps = {
  entity?: Entity;
  setSnackbarMessage: (message: SnackMessage) => void;
  setSnackbarOpen: (open: boolean) => void;
};

const AttachButton = ({
  entity,
  setSnackbarMessage,
  setSnackbarOpen,
}: AttachButtonProps) => {
  const [loading, setLoading] = useState(false);

  const handleClick = async () => {
    setLoading(true);
    // Call the attach or detach function depending on the isAttached value
    // and await for the result
    try {
      let response = await (entity?.attached
        ? detachEntity({ entity_did: entity?.did })
        : attachEntity({ entity_did: entity?.did }));

      if (!entity?.attached) {
        console.log("calling isAttached");
        response = await isAttached({ entity_did: entity?.did });
        console.log("response: ", response);
      }
      const msg = {
        message: response.data.message,
        severity: "success",
      } as SnackMessage;
      setSnackbarMessage(msg);
      setSnackbarOpen(true);
    } catch (error) {
      if (axios.isAxiosError(error)) {
        // Extract the error message from the error object
        const errorMessage = error.response?.data.detail[0].msg;

        const msg = {
          message: `${errorMessage}`,
          severity: "error",
        } as SnackMessage;
        setSnackbarMessage(msg);
        setSnackbarOpen(true);
      } else {
        console.error("error: ", error);
      }
    } finally {
      setLoading(false);
    }
  };

  return (
    <>
      <Button
        onClick={handleClick}
        className="mr-6"
        variant="contained"
        // Disable the button while loading
        disabled={loading}
      >
        {loading ? (
          <CircularProgress size={24} />
        ) : entity?.attached ? (
          "Detach"
        ) : (
          "Attach"
        )}
      </Button>
    </>
  );
};

export default function Client({
  params,
}: {
  params: { client_name: string };
}) {
  const { client_name } = params;

  const { entity: entity } = useGetEntityByNameOrDid(client_name);
  const {
    data: services,
    isLoading: services_loading,
    swrKey: entityKeyFunc,
  } = useGetAllServices();

  const clients: Service[] = useMemo(() => {
    if (services?.data) {
      return services.data.filter((service) => {
        if (service.entity_did !== entity?.did) return true;
      });
    }
    return [];
  }, [services, entity?.did]);

  const onRefresh = () => {
    const entityKey =
      typeof entityKeyFunc === "function" ? entityKeyFunc() : entityKeyFunc;
    if (entityKey) mutate(entityKey);
  };

  useEffect(() => {
    const interval = setInterval(() => {
      onRefresh();
    }, 5000);

    return () => clearInterval(interval);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  const cardContentRef = useRef(null);
  const [snackbarOpen, setSnackbarOpen] = useState(false);
  const [snackbarMessage, setSnackbarMessage] = useState<
    SnackMessage | undefined
  >(undefined);

  const closeSnackBar = () => {
    setSnackbarMessage(undefined);
    setSnackbarOpen(false);
  };

  console.log("entity", entity);

  if (services_loading) return <Skeleton height={500} />;
  if (!services) return <Alert severity="error">Client not found</Alert>;

  return (
    <div className="m-10">
      <div
        style={{
          display: "flex",
          alignItems: "center",
          justifyContent: "space-between",
        }}
      >
        <h2>Entity {entity?.name}</h2>
        <div>
          <AttachButton
            entity={entity}
            setSnackbarMessage={setSnackbarMessage}
            setSnackbarOpen={setSnackbarOpen}
          ></AttachButton>

          <Button onClick={onRefresh} variant="contained">
            Refresh
          </Button>
        </div>
      </div>

      <Card variant="outlined">
        <CardHeader
          subheader="Summary"
          action={<CopyToClipboard contentRef={cardContentRef} />}
        />
        <CardContent ref={cardContentRef}>
          <Typography color="text.primary" gutterBottom>
            DID: <code>{entity?.did}</code>
          </Typography>
          <Typography color="text.primary" gutterBottom>
            IP: <code>{entity?.ip}</code>
          </Typography>
          <Typography color="text.primary" gutterBottom>
            Network: <code>{entity?.network}</code>
          </Typography>
        </CardContent>
      </Card>
      <div>
        <h4>Client View</h4>
        <CustomTable
          loading={services_loading}
          data={clients}
          configuration={ClientTableConfig}
          tkey="client-table"
        />
      </div>
      <div>
        <h4>Service View</h4>
        <CustomTable
          loading={services_loading}
          data={services?.data}
          configuration={ServiceTableConfig}
          tkey="service-table"
        />
      </div>
      <Snackbar
        onClose={closeSnackBar}
        anchorOrigin={{ vertical: "top", horizontal: "center" }}
        open={snackbarOpen}
        autoHideDuration={5000}
      >
        <Alert
          severity={snackbarMessage?.severity}
          // Add some margin or padding to the Alert component
          sx={{ width: "100%", margin: 1, padding: 2 }}
          // Add an IconButton component with a CloseIcon inside the Alert component
          action={
            <IconButton
              size="small"
              aria-label="close"
              color="inherit"
              onClick={closeSnackBar}
            >
              <CloseIcon fontSize="small" />
            </IconButton>
          }
        >
          {snackbarMessage?.message}
        </Alert>
      </Snackbar>
    </div>
  );
}
