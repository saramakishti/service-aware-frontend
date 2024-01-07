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
} from "@mui/material";
import CopyToClipboard from "@/components/copy_to_clipboard";
import { useGetServicesByName } from "@/api/services/services";
import { attachEntity, detachEntity } from "@/api/entities/entities";
import { mutate } from "swr";
import { Skeleton } from "@mui/material";
import { Service } from "@/api/model";

export default function Client({
  params,
}: {
  params: { client_name: string };
}) {
  const { client_name } = params;

  const {
    data: services,
    isLoading: services_loading,
    swrKey: entityKeyFunc,
  } = useGetServicesByName({
    entity_name: client_name,
  });

  const entity = services?.data?.entity;
  const clients: Service[] = useMemo(() => {
    if (services?.data?.services) {
      return services.data.services.filter((service) => {
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
  const [snackbarMessage, setSnackbarMessage] = useState("");
  const [isAttached, setIsAttached] = useState(entity?.attached);

  const closeSnackBar = () => {
    setSnackbarMessage("");
    setSnackbarOpen(false);
  };

  const onAttachEntity = async () => {
    try {
      if (entity) {
        const response = await attachEntity(entity.did);
        setSnackbarMessage(response.data.message);
        setSnackbarOpen(true);
      } else {
        console.error("no entity");
      }
    } catch (error) {
      console.error(error);
    } finally {
      setIsAttached(true);
    }
  };

  const onDetachEntity = async () => {
    try {
      if (entity) {
        const response = await detachEntity(entity.did);
        console.log(response);
        setSnackbarMessage("Entity detached successfully.");
        setSnackbarOpen(true);
      } else {
        console.error("no entity");
      }
    } catch (error) {
      console.error(error);
    } finally {
      setIsAttached(false);
    }
  };

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
        <h2>Client 1</h2>
        <div>
          {isAttached === false ? (
            <Button
              onClick={onAttachEntity}
              className="mr-6"
              variant="contained"
            >
              Attach
            </Button>
          ) : (
            <Button
              onClick={onDetachEntity}
              className="mr-6"
              variant="contained"
            >
              Detach
            </Button>
          )}

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
            Network: <code>{entity?.other?.network}</code>
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
          data={services?.data?.services}
          configuration={ServiceTableConfig}
          tkey="service-table"
        />
      </div>
      <Snackbar
        onClose={closeSnackBar}
        anchorOrigin={{ vertical: "top", horizontal: "center" }}
        open={snackbarOpen}
        autoHideDuration={1000}
      >
        <Alert severity="success" sx={{ width: "100%" }}>
          {snackbarMessage}
        </Alert>
      </Snackbar>
    </div>
  );
}
