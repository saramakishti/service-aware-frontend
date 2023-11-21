"use client";

import SummaryDetails from "@/components/summary_card";
import CustomTable from "@/components/table";
import {
  APSummaryDetails,
  APAttachmentsDummyData,
  APAttachmentsTableConfig,
  APServiceRepositoryDummyData,
  APServiceRepositoryTableConfig,
} from "@/mock/access_point";

export default function AccessPoint() {
  return (
    <div className="m-10">
      <SummaryDetails
        hasRefreshButton
        entity={{ name: "Access Point", details: APSummaryDetails }}
      />
      <div>
        <h4>Attachement View</h4>
        <CustomTable
          data={APAttachmentsDummyData}
          configuration={APAttachmentsTableConfig}
        />
      </div>
      <div>
        <h4>Service Repository View </h4>
        <CustomTable
          data={APServiceRepositoryDummyData}
          configuration={APServiceRepositoryTableConfig}
        />
      </div>
    </div>
  );
}
