// AP - Summary

export const APSummaryDetails = [
  {
    label: "DID",
    value: "did:sov:test:1274",
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

// AP - Attachements

export const APAttachmentsDummyData = [
  {
    entity_name: "C1",
    entity_did: "did:sov:test:1234",
    network: "Carlo's Home Network",
    ip_address: "127.0.0.1",
  },
  {
    entity_name: "C2",
    entity_did: "did:sov:test:4567",
    network: "Steve's Home Network",
    ip_address: "127.0.0.1",
  },
  {
    entity_name: "C1-TEST",
    entity_did: "did:sov:test:0001",
    network: "Test Network A",
    ip_address: "127.0.0.1",
  },
  {
    entity_name: "C2-TEST",
    entity_did: "did:sov:test:0002",
    network: "Test Network B",
    ip_address: "127.0.0.1",
  },
];
export const APAttachmentsTableConfig = [
  {
    key: "entity_name",
    label: "Entity name",
  },
  {
    key: "entity_did",
    label: "Entity DID",
  },
  {
    key: "network",
    label: "Network",
  },
  {
    key: "ip_address",
    label: "IP address",
  },
];

// AP - Service Repository
export const APServiceRepositoryDummyData = [
  {
    service_name: "Carlo's Printing",
    service_type: "3D Printing",
    endpoint_url: "URL",
    entity: "C1",
    entity_did: "did:sov:test:1234",
    network: "Carlo's Home Network",
  },
  {
    service_name: "Jeff's Printing",
    service_type: "3D Printing",
    endpoint_url: "URL",
    entity: "C2",
    entity_did: "did:sov:test:5678",
    network: "Jeff's Home Network",
  },
];
export const APServiceRepositoryTableConfig = [
  {
    key: "service_name",
    label: "Service name",
  },
  {
    key: "service_type",
    label: "Service type",
  },
  {
    key: "endpoint_url",
    label: "End point",
  },
  {
    key: "entity",
    label: "Entity",
  },
  {
    key: "entity_did",
    label: "Entity DID",
  },
  {
    key: "network",
    label: "Network",
  },
];
