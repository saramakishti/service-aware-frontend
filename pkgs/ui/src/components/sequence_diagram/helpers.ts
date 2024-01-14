export const generateMermaidString = (data: any) => {
  if (!data || data.length === 0) return "";

  // Extract unique participants
  const participants = Array.from(
    new Set(
      data
        .map((item: any) => item.src_did)
        .concat(data.map((item: any) => item.des_did)),
    ),
  );

  // Begin the sequence diagram definition
  let mermaidString = "sequenceDiagram\n";

  // Add participants to the diagram
  participants.forEach((participant, index) => {
    mermaidString += `  participant ${String.fromCharCode(
      65 + index,
    )} as ${participant}\n`;
  });

  // Add messages to the diagram
  data.forEach((item: any, index: number) => {
    const srcParticipant = String.fromCharCode(
      65 + participants.indexOf(item.src_did),
    );
    const desParticipant = String.fromCharCode(
      65 + participants.indexOf(item.des_did),
    );
    const timestamp = new Date(item.timestamp * 1000).toLocaleString(); // Convert Unix timestamp to readable date
    const message = item.msg.text || `Event message ${index + 1}`;

    // If group_name or group_id exists, start an 'alt' block
    if (item.group_id != null) {
      mermaidString += `  alt ${item.group_name || item.group_id}\n`;
      mermaidString += `    rect rgb(191, 223, 255)\n`;
    }

    // Add the message interaction
    mermaidString += `  ${srcParticipant}->>${desParticipant}: [${timestamp}] ${message}\n`;

    // If there was an 'alt' block, close it
    if (item.group_id != null) {
      mermaidString += `    end\n`;
      mermaidString += `  end\n`;
    }
  });

  return mermaidString;
};

// Dummy Data

export const dataFromBE = [
  {
    id: 12,
    timestamp: 1704892813,
    group: 0,
    group_id: 12,
    // "group_name": "Data",
    msg_type: 4,
    src_did: "did:sov:test:121",
    // "src_name": "Entity A",
    des_did: "did:sov:test:120",
    // "des_name": "Entity B",
    msg: {
      text: "Hello World",
    },
  },
  {
    id: 60,
    timestamp: 1704892823,
    group: 1,
    group_id: 19,
    msg_type: 4,
    src_did: "did:sov:test:122",
    des_did: "did:sov:test:121",
    msg: {},
  },
  {
    id: 30162,
    timestamp: 1704892817,
    group: 1,
    group_id: 53,
    msg_type: 2,
    src_did: "did:sov:test:121",
    des_did: "did:sov:test:122",
    msg: {},
  },
  {
    id: 63043,
    timestamp: 1704892809,
    group: 0,
    group_id: 12,
    msg_type: 3,
    src_did: "did:sov:test:121",
    des_did: "did:sov:test:120",
    msg: {},
  },
  {
    id: 66251,
    timestamp: 1704892805,
    group: 0,
    group_id: 51,
    msg_type: 1,
    src_did: "did:sov:test:120",
    des_did: "did:sov:test:121",
    msg: {},
  },
  {
    id: 85434,
    timestamp: 1704892807,
    group: 0,
    group_id: 51,
    msg_type: 2,
    src_did: "did:sov:test:120",
    des_did: "did:sov:test:121",
    msg: {},
  },
  {
    id: 124842,
    timestamp: 1704892819,
    group: 1,
    group_id: 19,
    msg_type: 3,
    src_did: "did:sov:test:122",
    des_did: "did:sov:test:121",
    msg: {},
  },
  {
    id: 246326,
    timestamp: 1704892815,
    group: 1,
    group_id: 53,
    msg_type: 1,
    src_did: "did:sov:test:121",
    des_did: "did:sov:test:122",
    msg: {},
  },
];
