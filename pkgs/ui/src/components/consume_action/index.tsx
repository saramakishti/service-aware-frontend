import { Button } from "@mui/material";
import useAxios from "../hooks/useAxios";
import { useState } from "react";

const ConsumeAction = ({ endpoint }: { endpoint: string }) => {

  const [currentEndpoint, setCurrentEndpoint] = useState("");
  const [shouldFetch, setShouldFetch] = useState(false);
  const { data, error } = useAxios(currentEndpoint, "GET", null, true, shouldFetch);

  if (error) console.error("Error consuming:", error);

  if (data) console.log('what the response', data)

  const onConsume = () => {
    setCurrentEndpoint(endpoint);
    setShouldFetch(true);
  }


  return <Button onClick={onConsume} variant="outlined">
    Consume
  </Button>
};

export default ConsumeAction;
