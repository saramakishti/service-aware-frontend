"use client";

import { DLGResolutionTableConfig, DLGSummaryDetails } from "@/config/dlg";
import CustomTable from "@/components/table";
import SummaryDetails from "@/components/summary_card";
import { useEffect } from "react";
import { useGetAllResolutions } from "@/api/resolution/resolution";
import { mutate } from "swr";

export default function DLG() {

  const {
    data: resolutionData,
    isLoading: loadingResolutions,
    swrKey: resolutionsKeyFunc,
  } = useGetAllResolutions();

  const onRefresh = () => {
    const resolutionsKey =
      typeof resolutionsKeyFunc === "function"
        ? resolutionsKeyFunc()
        : resolutionsKeyFunc;

    if (resolutionsKey) {
      mutate(resolutionsKey);
    }
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
          data={resolutionData?.data}
          configuration={DLGResolutionTableConfig}
          tkey="resolution_table"
        />
      </div>
    </div>
  );
}
