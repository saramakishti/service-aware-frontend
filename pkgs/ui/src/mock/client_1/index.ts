// Client1 - Summary

export const Client1SummaryDetails = [
  {
    label: "DID",
    value: "did:sov:test:1234",
  },
  {
    label: "IP",
    value: "127.0.0.1",
  },
  {
    label: "Network",
    value: "Carlo's Home Network",
  },
];

export const Client1ConsumerData = [
  {
    "service_name": "Carlo's Printing",
    "service_type": "3D Printing",
    "end_point": "Consume",
    "producer": "C2",
    "producer_did": "did:sov:test:1223",
    "network": "Carlo's Home Network",
  },
  {
    "service_name": "Steve's Printing",
    "service_type": "3D Printing",
    "end_point": "Consume",
    "producer": "C2",
    "producer_did": "did:sov:test:1234",
    "network": "Steve's Home Network",
  },
  {
    "service_name": "Test A",
    "service_type": "3D Printing",
    "end_point": "Consume",
    "producer": "C2",
    "producer_did": "did:sov:test:4567",
    "network": "Test Network A",
  },
  {
    "service_name": "Test B",
    "service_type": "3D Printing",
    "end_point": "Consume",
    "producer": "C2",
    "producer_did": "did:sov:test:0062",
    "network": "Test Network B",
  },

]


export const Client1ConsumerTableConfig = [
  {
    key: "service_name",
    label: "Service name"
  },
  {
    key: "service_type",
    label: "Service Type"
  },
  {
    key: "end_point",
    label: "End Point"
  },
  {
    key: "producer",
    label: "Producer"
  },
  {
    key: "producer_did",
    label: "Producer DID"
  },
  {
    key: "network",
    label: "Network"
  }
]
