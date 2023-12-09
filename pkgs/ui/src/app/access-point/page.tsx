"use client";

import SummaryDetails from "@/components/summary_card";
import CustomTable from "@/components/table";
import {
  APSummaryDetails,
  APAttachmentsDummyData,
  APAttachmentsTableConfig,
  APServiceRepositoryTableConfig,
} from "@/mock/access_point";
import { useEffect, useState } from "react";

interface RepositoryData {
  entity_name: string;
  entity_did: string;
  network: string;
  ip_address: string;
}

export default function AccessPoint() {
  const [repositoryData, setRepositoryData] = useState<RepositoryData[]>([]);

  useEffect(() => {
    fetch("http://localhost:2979/api/v1/get_repositories", {
      method: "GET",
      // credentials: 'include',
    })
      .then((resp) =>
        resp.json().then((jsonData) => {
          console.log(jsonData);

          const transformedData = jsonData.map((item: { service_name: any; entity_did: any; network: any; }) => ({
            entity_name: item.service_name,
            entity_did: item.entity_did,
            network: item.network,
            ip_address: "",
          }));

          setRepositoryData(transformedData);
        }),
      )
      .then()
      .catch();
  }, []);

  return (
    <div className="m-10">
      <SummaryDetails
        hasRefreshButton
        entity={{ name: "Access Point", details: APSummaryDetails }}
      />
      <div>
        <h4>Attachment View</h4>
        <CustomTable
          data={APAttachmentsDummyData}
          configuration={APAttachmentsTableConfig}
        />
      </div>
      <div>
        <h4>Service Repository View </h4>
        <CustomTable
          data={repositoryData}
          configuration={APServiceRepositoryTableConfig}
        />
      </div>
    </div>
  );
}
