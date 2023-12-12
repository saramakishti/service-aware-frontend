"use client";

import { DLGResolutionTableConfig, DLGSummaryDetails } from "@/config/dlg";
import CustomTable from "@/components/table";
import SummaryDetails from "@/components/summary_card";
import useFetch from "@/components/hooks/useFetch";
import { useEffect } from "react";

export default function DLG() {
  const {
    data: resolutionData,
    loading: loadingResolutions,
    fetch,
  } = useFetch("/get_resolutions");

  const onRefresh = () => {
    fetch();
  };

  useEffect(() => {
    const interval = setInterval(() => {
      onRefresh();
    }, 5000);

    return () => clearInterval(interval);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  return (
    <div className="m-10">
      <SummaryDetails
        fake
        hasRefreshButton
        onRefresh={onRefresh}
        entity={{
          name: "Distributed Ledger Gateway",
          details: DLGSummaryDetails,
        }}
      />
      <div>
        <h4>DID Resolution View</h4>
        <CustomTable
          loading={loadingResolutions}
          data={resolutionData}
          configuration={DLGResolutionTableConfig}
        />
      </div>
    </div>
  );
}
