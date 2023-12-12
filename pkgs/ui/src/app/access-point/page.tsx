"use client";

import { mutate } from "swr";
import { useGetAttachedEntities } from "@/api/entities/entities";
import { useGetRepositories } from "@/api/repositories/repositories";
import SummaryDetails from "@/components/summary_card";
import CustomTable from "@/components/table";
import {
  APSummaryDetails,
  APAttachmentsTableConfig,
  APServiceRepositoryTableConfig,
} from "@/config/access_point";
import { useEffect } from "react";

export default function AccessPoint() {
  const {
    data: APAttachementData,
    isLoading: loadingAttachements,
    swrKey: attachedEntitiesKeyFunc,
  } = useGetAttachedEntities();
  const {
    data: APRepositories,
    isLoading: laodingRepositories,
    swrKey: repositoriesKeyFunc,
  } = useGetRepositories();

  const onRefresh = () => {
    const attachedEntitiesKey =
      typeof attachedEntitiesKeyFunc === "function"
        ? attachedEntitiesKeyFunc()
        : attachedEntitiesKeyFunc;
    const repositoriesKey =
      typeof repositoriesKeyFunc === "function"
        ? repositoriesKeyFunc()
        : repositoriesKeyFunc;

    if (attachedEntitiesKey) {
      mutate(attachedEntitiesKey);
    }
    if (repositoriesKey) {
      mutate(repositoriesKey);
    }
  };

  useEffect(() => {
    const interval = setInterval(() => {
      onRefresh();
    }, 1000);

    return () => clearInterval(interval);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  return (
    <div className="m-10">
      <SummaryDetails
        fake
        hasRefreshButton
        onRefresh={onRefresh}
        entity={{ name: "Access Point", details: APSummaryDetails }}
      />
      <div>
        <h4>Attachment View</h4>
        <CustomTable
          loading={loadingAttachements}
          data={APAttachementData?.data}
          configuration={APAttachmentsTableConfig}
        />
      </div>
      <div>
        <h4>Service Repository View </h4>
        <CustomTable
          loading={laodingRepositories}
          data={APRepositories?.data}
          configuration={APServiceRepositoryTableConfig}
        />
      </div>
    </div>
  );
}
