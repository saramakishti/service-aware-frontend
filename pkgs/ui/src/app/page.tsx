"use client";
import { RecentActivity } from "@/components/dashboard/activity";
import { useAppState } from "@/components/hooks/useAppContext";
import { LoadingOverlay } from "@/components/join/loadingOverlay";

export default function Dashboard() {
  const { isLoading } = useAppState();
  if (isLoading) {
    return (
      <div className="grid h-full place-items-center">
        <div className="mt-8 w-full max-w-xl">
          <LoadingOverlay
            title="Clan Experience"
            subtitle="Loading"
            variant="circle"
          />
        </div>
      </div>
    );
  } else {
    return (
      <div className="flex w-full">
        <div className="grid w-full grid-flow-row grid-cols-3 gap-4">
          <div className="row-span-2">
            <RecentActivity />
          </div>
        </div>
      </div>
    );
  }
}
