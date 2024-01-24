import { Eventmessage } from "@/api/model";

export const generateMermaidString = (data: Eventmessage[] | undefined) => {
  if (!data) return "";

  let mermaidString = "";

  // We'll use a Set to ensure participant uniqueness
  const participants: Set<string> = new Set();

  // Define colors for groups (if you have more groups, add more colors)
  const groupColors: Record<number, string> = {
    0: "rgb(191, 223, 255)",
    1: "rgb(200, 150, 255)",
    // Add more group colors if needed
  };

  // Loop through the groups and group_ids to build the string
  Object.entries(data).forEach(([group, groupData]) => {
    // Add a rectangle for each group with a note
    mermaidString += `  rect ${
      groupColors[parseInt(group)] || "rgb(128, 128, 128)"
    }\n`; // Fallback color if not defined
    mermaidString += `  Note over ${Object.values(groupData)
      .flatMap((gd) => gd.map((msg: any) => msg.src_name))
      .join(",")}: Group ${group}\n`;

    Object.entries(groupData).forEach(([groupId, messages]) => {
      // Add a rectangle for each group_id with a note
      mermaidString += `  alt Group ID ${groupId}\n`;

      messages.forEach((msg: any) => {
        // Ensure we include each participant
        participants.add(msg.src_name);
        participants.add(msg.des_name);

        // Add each message
        mermaidString += `  ${msg.src_name}->>${msg.des_name}: [${msg.msg_type_name}]: Event Message ${msg.id}\n`;
      });

      mermaidString += `  end\n`;
    });

    mermaidString += `  end\n`;
  });

  // Add participants at the start of the string
  const participantString = Array.from(participants)
    .map((participant) => {
      return `  participant ${participant}\n`;
    })
    .join("");

  // Prepend participants to the mermaidString
  mermaidString = `sequenceDiagram\n${participantString}` + mermaidString;

  return mermaidString;
};

export const mermaidSample = `
sequenceDiagram
    participant C0 as C0 <br/>did:sov:test:120
    participant C1 as C1 <br/>did:sov:test:121
    participant C2 as C2 <br/>did:sov:test:122

    rect rgb(255, 154, 162)
    Note over C0,C1 : Group 0
    alt Group Id 16
    C1->>C0: [Presentation]: Event Message 1
    C1->>C0: [DID Resolution]: Event Message 2
    end

    alt Group Id 51
    C0->>C1: [Attachement]: Event Message 3
    C0->>C1: [Connection Setup]: Event Message 4
    end
    end

    rect rgb(254, 183, 177)
    Note over C1,C2 : Group 1
    alt Group Id 13
    C2->>C1: [Presentation]: Event Message 5
    C2->>C1: [DID Resolution]: Event Message 6
    end

    alt Group Id 21
    C1->>C2: [Attachement]: Event Message 7
    C1->>C2: [Connection Setup]: Event Message 8
    end
    end

    rect rgb(255, 218, 192)
    Note over C0,C1 : Group 0
    alt Group Id 16
    C1->>C0: [Presentation]: Event Message 1
    C1->>C0: [DID Resolution]: Event Message 2
    end

    alt Group Id 51
    C0->>C1: [Attachement]: Event Message 3
    C0->>C1: [Connection Setup]: Event Message 4
    end
    end

    rect rgb(255, 236, 196)
    Note over C1,C2 : Group 1
    alt Group Id 13
    C2->>C1: [Presentation]: Event Message 5
    C2->>C1: [DID Resolution]: Event Message 6
    end

    alt Group Id 21
    C1->>C2: [Attachement]: Event Message 7
    C1->>C2: [Connection Setup]: Event Message 8
    end
    end

    rect rgb(226, 240, 204)
    Note over C0,C1 : Group 0
    alt Group Id 16
    C1->>C0: [Presentation]: Event Message 1
    C1->>C0: [DID Resolution]: Event Message 2
    end

    alt Group Id 51
    C0->>C1: [Attachement]: Event Message 3
    C0->>C1: [Connection Setup]: Event Message 4
    end
    end

    rect rgb(181, 234, 214)
    Note over C1,C2 : Group 1
    alt Group Id 13
    C2->>C1: [Presentation]: Event Message 5
    C2->>C1: [DID Resolution]: Event Message 6
    end

    alt Group Id 21
    C1->>C2: [Attachement]: Event Message 7
    C1->>C2: [Connection Setup]: Event Message 8
    end
    end

    rect rgb(183, 219, 235)
    Note over C0,C1 : Group 0
    alt Group Id 16
    C1->>C0: [Presentation]: Event Message 1
    C1->>C0: [DID Resolution]: Event Message 2
    end

    alt Group Id 51
    C0->>C1: [Attachement]: Event Message 3
    C0->>C1: [Connection Setup]: Event Message 4
    end
    end

    rect rgb(199, 206, 234)
    Note over C1,C2 : Group 1
    alt Group Id 13
    C2->>C1: [Presentation]: Event Message 5
    C2->>C1: [DID Resolution]: Event Message 6
    end

    alt Group Id 21
    C1->>C2: [Attachement]: Event Message 7
    C1->>C2: [Connection Setup]: Event Message 8
    end
    end
`;

export const eventMessages = [
  {
    timestamp: 1706034368,
    group: 0,
    group_id: 16,
    msg_type: 3,
    src_did: "did:sov:test:121",
    des_did: "did:sov:test:120",
    msg: {},
    id: 3,
    des_name: "C0",
    src_name: "C1",
    msg_type_name: "Presentation",
  },
  {
    timestamp: 1706034372,
    group: 0,
    group_id: 16,
    msg_type: 4,
    src_did: "did:sov:test:121",
    des_did: "did:sov:test:120",
    msg: {},
    id: 4,
    des_name: "C0",
    src_name: "C1",
    msg_type_name: "DID Resolution",
  },
  {
    timestamp: 1706034364,
    group: 0,
    group_id: 51,
    msg_type: 1,
    src_did: "did:sov:test:120",
    des_did: "did:sov:test:121",
    msg: {},
    id: 1,
    des_name: "C1",
    src_name: "C0",
    msg_type_name: "Attachement",
  },
  {
    timestamp: 1706034366,
    group: 0,
    group_id: 51,
    msg_type: 2,
    src_did: "did:sov:test:120",
    des_did: "did:sov:test:121",
    msg: {},
    id: 2,
    des_name: "C1",
    src_name: "C0",
    msg_type_name: "Connection Setup",
  },
  {
    timestamp: 1706034378,
    group: 1,
    group_id: 13,
    msg_type: 3,
    src_did: "did:sov:test:122",
    des_did: "did:sov:test:121",
    msg: {},
    id: 7,
    des_name: "C1",
    src_name: "C2",
    msg_type_name: "Presentation",
  },
  {
    timestamp: 1706034382,
    group: 1,
    group_id: 13,
    msg_type: 4,
    src_did: "did:sov:test:122",
    des_did: "did:sov:test:121",
    msg: {},
    id: 8,
    des_name: "C1",
    src_name: "C2",
    msg_type_name: "DID Resolution",
  },
  {
    timestamp: 1706034374,
    group: 1,
    group_id: 21,
    msg_type: 1,
    src_did: "did:sov:test:121",
    des_did: "did:sov:test:122",
    msg: {},
    id: 5,
    des_name: "C2",
    src_name: "C1",
    msg_type_name: "Attachement",
  },
  {
    timestamp: 1706034376,
    group: 1,
    group_id: 21,
    msg_type: 2,
    src_did: "did:sov:test:121",
    des_did: "did:sov:test:122",
    msg: {},
    id: 6,
    des_name: "C2",
    src_name: "C1",
    msg_type_name: "Connection Setup",
  },
];
