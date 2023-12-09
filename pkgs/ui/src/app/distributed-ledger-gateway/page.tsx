"use client";

import {
  DLGResolutionTableConfig,
  DLGSummaryDetails,
} from "@/mock/dlg";
import CustomTable from "@/components/table";
import SummaryDetails from "@/components/summary_card";
import {useEffect, useState} from "react";

export default function DLG() {
  const [resolutionData, setResolutionData] = useState([]);

  useEffect(() => {
    fetch("http://localhost:2979/api/v1/get_resolutions", {
      method: "GET",
    })
      .then((resp) =>
        resp.json().then((jsonData) => {
          console.log(jsonData);
          setResolutionData(jsonData);
        }),
      )
      .then()
      .catch();
  }, []);

  return (
    <div className="m-10">
      <SummaryDetails
        hasRefreshButton
        entity={{
          name: "Distributed Ledger Gateway",
          details: DLGSummaryDetails,
        }}
      />
      <div>
        <h4>DID Resolution View</h4>
        <CustomTable
          data={resolutionData}
          configuration={DLGResolutionTableConfig}
        />
      </div>
    </div>
  );
}
