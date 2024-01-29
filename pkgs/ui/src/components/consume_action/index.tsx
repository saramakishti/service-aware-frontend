import { Button, CircularProgress, Snackbar } from "@mui/material";
import { useState } from "react";
import axios from "axios";

const ConsumeAction = ({
  endpoint,
  onConsume,
}: {
  endpoint: string;
  rowData?: any;
  onConsume?: any;
}) => {
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(false);

  if (error) console.error("Error in state", error);

  const handleConsume = () => {
    if (loading) return;

    setLoading(true);

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
        if (onConsume) {
          onConsume(response.data);
          console.log("I got the data from consume: ", response.data);
        }
      })
      .catch((error) => {
        if (onConsume) onConsume(null);
        console.error("Error happened during consume: ", error);
        setError(error);
      })
      .finally(() => {
        setLoading(false);
      });
  };

  const handleCloseSnackbar = () => {
    setError(null);
  };

  return (
    <>
      <Button disabled={loading} onClick={handleConsume} variant="contained">
        {loading ? <CircularProgress size={24} /> : `Consume`}
      </Button>
      {error && (
        <Snackbar
          anchorOrigin={{ vertical: "top", horizontal: "center" }}
          open={error}
          autoHideDuration={2000}
          message={`Something happened during consume: ${error}`}
          onClose={handleCloseSnackbar}
        />
      )}
    </>
  );
};

export default ConsumeAction;
