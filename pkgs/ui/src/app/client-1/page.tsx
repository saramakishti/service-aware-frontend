"use client";

import SummaryDetails from "@/components/summary_card";
import {
  Client1SummaryDetails,
  Client1ConsumerData,
  Client1ConsumerTableConfig,
  Client1ProducerTableConfig,
  Client1ProducerData,
} from "@/mock/client_1";
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
          jsonData.length > 0
            ? setConsumerData(jsonData)
            : setConsumerData(Client1ConsumerData);
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
          jsonData.length > 0
            ? setProducerData(jsonData)
            : setProducerData(Client1ProducerData);
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
          name: "Client 1",
          details: Client1SummaryDetails,
        }}
      />
      <div>
        <h4>Consumer View</h4>
        <CustomTable
          data={consumerData}
          configuration={Client1ConsumerTableConfig}
        />
      </div>
      <div>
        <h4>Producer View</h4>
        <CustomTable
          data={producerData}
          configuration={Client1ProducerTableConfig}
        />
      </div>
    </div>
  );
}
