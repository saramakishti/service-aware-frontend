"use client";
import { useEffect, useRef, useState } from "react";
import {
  Client2ConsumerTableConfig,
  Client2ProducerTableConfig,
} from "@/config/client_2";
import CustomTable from "@/components/table";
import useGetEntityByName from "@/components/hooks/useGetEntityById";
import {
  Button,
  Card,
  CardContent,
  CardHeader,
  Skeleton,
  Typography,
  Snackbar,
  Alert,
} from "@mui/material";
import CopyToClipboard from "@/components/copy_to_clipboard";
import { useGetEntity } from "@/api/entities/entities";
import { mutate } from "swr";
import axios from "axios";
import { BASE_URL } from "@/constants";

export default function Client2() {
  const { entity } = useGetEntityByName("C2");
  const {
    data: client2,
    isLoading,
    swrKey: entityKeyFunc,
  } = useGetEntity({ entity_did: entity?.did });
  const cardContentRef = useRef(null);
  const [isAttached, setIsAttached] = useState(entity?.attached);
  const [snackbarOpen, setSnackbarOpen] = useState(false);
  const [snackbarMessage, setSnackbarMessage] = useState("");

  const closeSnackBar = () => {
    setSnackbarMessage("");
    setSnackbarOpen(false);
  };

  const onAttachEntity = async () => {
    try {
      const response = await axios.post(`${BASE_URL}/attach`, {
        entity_did: entity?.did,
      });
      alert(response.data.message);
    } catch (error) {
      console.error(error);
    } finally {
      setIsAttached(true);
    }
  };

  const onDetachEntity = async () => {
    try {
      const response = await axios.post(`${BASE_URL}/detach`, {
        entity_did: entity?.did,
      });
      console.log("detach", response);
      alert("Entity Detached Successfully.");
    } catch (error) {
      console.error(error);
    } finally {
      setIsAttached(false);
    }
  };

  const onRefresh = () => {
    const entityKey =
      typeof entityKeyFunc === "function" ? entityKeyFunc() : entityKeyFunc;
    if (entityKey) mutate(entityKey);
  };

  useEffect(() => {
    const interval = setInterval(() => {
      onRefresh();
    }, 1000);

    return () => clearInterval(interval);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  if (isLoading) return <Skeleton height={500} />;

  return (
    <div className="m-10">
      <div
        style={{
          display: "flex",
          alignItems: "center",
          justifyContent: "space-between",
        }}
      >
        <h2>Client 2</h2>
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
            DID: <code>{client2?.data?.did}</code>
          </Typography>
          <Typography color="text.primary" gutterBottom>
            IP: <code>{client2?.data?.ip}</code>
          </Typography>
          <Typography color="text.primary" gutterBottom>
            Network: <code>{client2?.data?.other?.network}</code>
          </Typography>
        </CardContent>
      </Card>
      <div>
        <h4>Consumer View</h4>
        <CustomTable
          loading={isLoading}
          data={client2?.data?.producers}
          configuration={Client2ConsumerTableConfig}
        />
      </div>
      <div>
        <h4>Producer View</h4>
        <CustomTable
          loading={isLoading}
          data={client2?.data?.producers}
          configuration={Client2ProducerTableConfig}
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
