import { IEntityActions } from "@/types";
import {
  Button,
  Snackbar,
  Alert,
  AlertColor,
  CircularProgress,
} from "@mui/material";
import { useState } from "react";
import { deleteEntity } from "@/api/entities/entities";
import axios from "axios";

interface Props {
  endpointData: IEntityActions[];
  rowData?: any;
}

const SNACKBAR_DEFAULT = {
  open: false,
  message: "",
  severity: "info" as AlertColor,
};

const EntityActions = ({ endpointData, rowData }: Props) => {
  const [snackbar, setSnackbar] = useState<{
    open: boolean;
    message: string;
    severity: AlertColor;
  }>(SNACKBAR_DEFAULT);

  const [registerData, setRegisterData] = useState(null);
  const [registerError, setRegisterError] = useState(null);
  const [loadingRegister, setLoadingRegister] = useState(false);

  const [DeregisterData, setDeRegisterData] = useState(null);
  const [DeregisterError, setDeRegisterError] = useState(null);
  const [loadingDeRegister, setLoadingDeRegister] = useState(false);

  const [loadingDelete, setLoadingDelete] = useState(false);

  if (registerData) console.log("Register Data in state", registerData);
  if (registerError) console.error("Register Error in state", registerError);

  if (DeregisterData) console.log("Register Data in state", DeregisterData);
  if (DeregisterError)
    console.error("Register Error in state", DeregisterError);

  const onDeleteEntity = async () => {
    setLoadingDelete(true);
    if (rowData)
      try {
        const response = await deleteEntity({
          entity_did: rowData?.entity_did,
        });
        setSnackbar({
          open: true,
          message: response.data.message,
          severity: "success",
        });
      } catch (error) {
        console.error("Error deleting entity: ", error);
        setSnackbar({
          open: true,
          message: "Failed to delete entity.",
          severity: "error",
        });
      } finally {
        setLoadingDelete(false);
      }
  };

  const onRegisterEntity = (endpoint: string) => {
    if (loadingRegister) return;

    setLoadingRegister(true);

    const axiosConfig = {
      url: endpoint,
      method: "GET",
      data: null,
      withCredentials: true,
      headers: {
        "Content-Type": "application/json",
        Accept: "application/json",
      },
    };

    axios(axiosConfig)
      .then((response) => {
        setRegisterData(response.data);
        console.log("I got the data from register: ", response.data);
      })
      .catch((error) => {
        console.error("Error happened during register: ", error);
        setRegisterError(error);
      })
      .finally(() => {
        setLoadingRegister(false);
      });
  };

  const onDeregisterEntity = (endpoint: string) => {
    if (loadingDeRegister) return;

    setLoadingDeRegister(true);

    const axiosConfig = {
      url: endpoint,
      method: "GET",
      data: null,
    };

    axios(axiosConfig)
      .then((response) => {
        setDeRegisterData(response.data);
        console.log("I got the data from deregister: ", response.data);
      })
      .catch((error) => {
        console.error("Error happened during deregister: ", error);
        setDeRegisterError(error);
      })
      .finally(() => {
        setLoadingDeRegister(false);
      });
  };

  const handleCloseSnackbar = () => {
    setSnackbar(SNACKBAR_DEFAULT);
  };

  return (
    <>
      <div className="flex justify-between">
        {endpointData.map(
          ({ name, endpoint }: IEntityActions, index: number) => {
            const isRegister = name && name.toLocaleLowerCase() === "register";
            // const isDeRegister = name && name.toLocaleLowerCase() === "deregister";
            return (
              <Button
                disabled={loadingRegister || loadingDeRegister}
                key={index}
                onClick={() =>
                  isRegister
                    ? onRegisterEntity(endpoint)
                    : onDeregisterEntity(endpoint)
                }
                variant="contained"
                size="small"
              >
                {name}
              </Button>
            );
          },
        )}
        <Button
          disabled={loadingDelete}
          onClick={onDeleteEntity}
          size="small"
          variant="contained"
        >
          {loadingDelete ? <CircularProgress size={24} /> : `Delete`}
        </Button>
      </div>
      <Snackbar
        anchorOrigin={{ vertical: "top", horizontal: "center" }}
        open={snackbar.open}
        autoHideDuration={5000}
        onClose={handleCloseSnackbar}
      >
        <Alert
          onClose={handleCloseSnackbar}
          severity={snackbar?.severity}
          sx={{ width: "100%" }}
        >
          {snackbar.message}
        </Alert>
      </Snackbar>
    </>
  );
};

export default EntityActions;
