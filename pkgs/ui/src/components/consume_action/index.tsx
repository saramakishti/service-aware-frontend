import { Button } from "@mui/material";
import { useState } from "react";
import axios from "axios";

const ConsumeAction = ({ endpoint }: { endpoint: string }) => {
  const [data, setData] = useState(null);
  const [error, setError] = useState(null);

  if (data) console.log("Data in state", data);
  if (error) console.log("Error in state", error);

  const onConsume = () => {
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
        setData(response.data);
        console.log("I got the data from consume: ", response.data);
      })
      .catch((error) => {
        console.error("Error happened during consume: ", error);
        setError(error);
      })
      .finally(() => {});
  };

  return (
    <Button onClick={onConsume} variant="outlined">
      Consume
    </Button>
  );
};

export default ConsumeAction;
