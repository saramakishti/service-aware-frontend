import { useState, useEffect } from "react";
import axios from "axios";
import { projectConfig } from "@/config/config";

const useAxios = (
  url: string,
  method = "GET",
  payload = null,
  isFullUrl = false,
  shouldFetch = false,
) => {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const fetch = () => {
    setLoading(true);
    setError(null);
    const finalUrl = isFullUrl ? url : projectConfig.BASE_URL + url;

    const axiosConfig = {
      url: finalUrl,
      method,
      data: payload,
    };

    axios(axiosConfig)
      .then((response) => {
        setData(response.data);
      })
      .catch((error) => {
        setError(error);
      })
      .finally(() => {
        setLoading(false);
      });
  };

  useEffect(() => {
    if (shouldFetch) {
      fetch();
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [url, method, JSON.stringify(payload), shouldFetch]);

  return { data, loading, error, refetch: fetch };
};

export default useAxios;
