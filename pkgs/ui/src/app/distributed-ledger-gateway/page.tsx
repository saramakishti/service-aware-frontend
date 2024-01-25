"use client";

import { DLGResolutionTableConfig } from "@/config/dlg";
import CustomTable from "@/components/table";
import SummaryDetails from "@/components/summary_card";
import { useEffect } from "react";
import { useGetAllResolutions } from "@/api/resolution/resolution";
import { mutate } from "swr";
import useGetEntityByNameOrDid from "@/components/hooks/useGetEntityByNameOrDid";
import { projectConfig } from "@/config/config";

export default function DLG() {
  const { entity } = useGetEntityByNameOrDid("DLG");
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
    }, projectConfig.REFRESH_FREQUENCY);

    return () => clearInterval(interval);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  return (
    <div className="m-10">
      <SummaryDetails
        hasRefreshButton
        onRefresh={onRefresh}
        entity={{
          name: "Distributed Ledger Gateway",
          details: [
            {
              label: "DID",
              value: entity?.did,
            },
            {
              label: "IP",
              value: entity?.ip,
            },
            {
              label: "Network",
              value: entity?.network,
            },
          ],
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
