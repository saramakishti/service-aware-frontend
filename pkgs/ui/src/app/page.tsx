"use client";
import { useAppState } from "@/components/hooks/useAppContext";
import { LoadingOverlay } from "@/components/join/loadingOverlay";
import Home from "./home/page";

export default function Dashboard() {
  const { isLoading } = useAppState();
  return isLoading ? (
    <div className="grid h-full place-items-center">
      <div className="mt-8 w-full max-w-xl">
        <LoadingOverlay
          title="Clan Experience"
          subtitle="Loading"
          variant="circle"
        />
      </div>
    </div>
  ) : (
    <Home />
  );
}
