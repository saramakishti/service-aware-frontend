"use client";

import { NoDataOverlay } from "@/components/noDataOverlay";
import SummaryDetails from "@/components/summary_card";
import CustomTable from "@/components/table";
import { HomeTableConfig } from "@/mock/home";
import { useEffect, useState } from "react";

export default function Home() {
  const [homeData, setHomeData] = useState([]);

  useEffect(() => {
    fetch("http://localhost:2979/api/v1/get_entities", {
      method: "GET",
      // credentials: 'include',
    })
      .then((resp) =>
        resp.json().then((jsonData) => {
          console.log(jsonData);
          setHomeData(jsonData);
        }),
      )
      .then()
      .catch();
  }, []);

  return (
    <div className="m-10">
      <SummaryDetails
        entity={{ name: "Home", details: [] }}
        hasRefreshButton={false}
        hasAttachDetach={false}
      />

      <div>
        <h4>Home View Table</h4>
        <CustomTable data={homeData} configuration={HomeTableConfig} />
      </div>

      <div>
        <h4>Sequence Diagram</h4>
        <NoDataOverlay label="No Activity yet" />
      </div>
    </div>
  );
}
