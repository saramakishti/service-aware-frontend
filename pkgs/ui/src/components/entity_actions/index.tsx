import { IEntityActions } from "@/types";
import { Button, Snackbar, Alert, AlertColor } from "@mui/material";
import { useState } from "react";
import useAxios from "../hooks/useAxios";
import { deleteEntity } from "@/api/entities/entities";

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
  const [currentEndpoint, setCurrentEndpoint] = useState("");
  const [shouldFetch, setShouldFetch] = useState(false);
  const { error } = useAxios(currentEndpoint, "GET", null, true, shouldFetch);

  const [snackbar, setSnackbar] = useState<{
    open: boolean;
    message: string;
    severity: AlertColor;
  }>(SNACKBAR_DEFAULT);

  console.error("Error registering/deregistering:", error);

  const onDeleteEntity = async () => {
    if (rowData)
      try {
        const response = await deleteEntity({
          entity_did: rowData?.entity_did,
        });
        console.log("On Delete:", response.data.message);
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
      }
  };

  const onRegisterEntity = (endpoint: string) => {
    setCurrentEndpoint(endpoint);
    setShouldFetch(true);
  };

  const onDeregisterEntity = (endpoint: string) => {
    setCurrentEndpoint(endpoint);
    setShouldFetch(true);
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
            return (
              <Button
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
        <Button onClick={onDeleteEntity} size="small" variant="contained">
          Delete
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
