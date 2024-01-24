import { useState, useEffect } from "react";
import axios from "axios";
import { projectConfig } from "@/config/config";

const useFetch = (url: string) => {
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const fetch = () => {
    setLoading(true);
    axios
      .get(projectConfig.BASE_URL + url)
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
    fetch();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [url]);

  return { data, loading, error, fetch };
};

export default useFetch;
