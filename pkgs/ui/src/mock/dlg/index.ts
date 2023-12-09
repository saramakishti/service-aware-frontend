// DLG Summary Details

export const DLGSummaryDetails = [
  {
    label: "DID",
    value: "did:sov:test:1274",
  },
  {
    label: "URL",
    value: "dlg.tu-berlin.de",
  },
];

// DLG Resolution Table

export const DLGResolutionDummyData = [
  {
    requester_name: "C1",
    requester_did: "did:sov:test:1234",
    resolved_did: "did:sov:test:1234",
    timestamp: "2023.11.01 17:05:45",
  },
  {
    requester_name: "C2",
    requester_did: "did:sov:test:5678",
    resolved_did: "did:sov:test:5678",
    timestamp: "2023.12.01 15:05:50",
  },
];

export const DLGResolutionTableConfig = [
  {
    key: "requester_name",
    label: "Requester name",
  },
  {
    key: "requester_did",
    label: "Requester DID",
  },
  {
    key: "resolved_did",
    label: "Resolved DID",
  },
  {
    key: "timestamp",
    label: "Timestamp",
  },
];
