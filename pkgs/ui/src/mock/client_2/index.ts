// Client2 - Summary

export const Client2SummaryDetails = [
  {
    label: "DID",
    value: "did:sov:test:1234",
  },
  {
    label: "IP",
    value: "127.0.0.2",
  },
  {
    label: "Network",
    value: "Carlo's Home Network",
  },
];

export const Client2ConsumerData = [
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

export const Client2ConsumerTableConfig = [
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

export const Client2ProducerData = [
  {
    "service_name": "Carlo's Printing",
    "service_type": "3D Printing",
    "end_point": "URL",
    "usage": "C1(3), C3(4)",
    "status": "DRAFT, REGISTERED",
    "action": "Register, Deregister, Delete",
  },
  {
    "service_name": "Steve's Printing",
    "service_type": "3D Printing",
    "end_point": "URL",
    "usage": "C1(3), C3(4)",
    "status": "REGISTERED",
    "action": "Create",
  },
  {
    "service_name": "Test Printing A",
    "service_type": "3D Printing",
    "end_point": "URL",
    "usage": "C1(3), C3(4)",
    "status": "DRAFT",
    "action": "Register, Deregister",
  },
  {
    "service_name": "Test Printing B",
    "service_type": "3D Printing",
    "end_point": "URL",
    "usage": "C1(3), C3(4)",
    "status": "DRAFT, REGISTERED",
    "action": "Delete, Create",
  },
]

export const Client2ProducerTableConfig = [
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
    key: "usage",
    label: "Usage"
  },
  {
    key: "status",
    label: "Status"
  },
  {
    key: "action",
    label: "Action"
  }
]
