import SummaryDetails from "@/components/summary_card";
import { Client2SummaryDetails } from "@/mock/client_2";

export default function Client1() {
  return (
    <div className="m-10">
      <SummaryDetails
        hasAttachDetach
        hasRefreshButton
        entity={{
          name: "Client 2",
          details: Client2SummaryDetails,
        }}
      />
    </div>
  );
}
