"use client";

import SummaryDetails from "@/components/summary_card";
import {
  Client2ConsumerTableConfig,
  Client2ProducerTableConfig,
  Client2SummaryDetails,
} from "@/mock/client_2";
import CustomTable from "@/components/table";
import { useEffect, useState } from "react";

export default function Client1() {
  const [consumerData, setConsumerData] = useState([]);
  const [producerData, setProducerData] = useState([]);

  useEffect(() => {
    fetch("http://localhost:2979/api/v1/get_consumers", {
      method: "GET",
      // credentials: 'include',
    })
      .then((resp) =>
        resp.json().then((jsonData) => {
          console.log(jsonData);
          setConsumerData(jsonData);
        }),
      )
      .then()
      .catch();

    fetch("http://localhost:2979/api/v1/get_producers", {
      method: "GET",
      // credentials: 'include',
    })
      .then((resp) =>
        resp.json().then((jsonData) => {
          console.log(jsonData);
          setProducerData(jsonData);
        }),
      )
      .then()
      .catch();
  }, []);

  return (
    <div className="m-10">
      <SummaryDetails
        hasAttachDetach
        hasRefreshButton
        entity={{
          name: "Client 2",
          details: Client2SummaryDetails,
        }}
      />
      <div>
        <h4>Consumer View</h4>
        <CustomTable
          data={consumerData}
          configuration={Client2ConsumerTableConfig}
        />
      </div>
      <div>
        <h4>Producer View</h4>
        <CustomTable
          data={producerData}
          configuration={Client2ProducerTableConfig}
        />
      </div>
    </div>
  );
}
