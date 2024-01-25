import { getGroupColor, sanitizeDID } from "@/utils/helpers";

export const generateMermaidString = (data: any) => {
  if (!data) return "";

  let mermaidString = "sequenceDiagram\n";
  const participantDetails = new Map();

  // Collect all unique participants along with their sanitized DIDs
  data.forEach((item: any) => {
    Object.values(item.groups).forEach((group: any) => {
      group.forEach((msg: any) => {
        // Apply sanitization to src_name and des_name if they are in DID format
        const sanitizedSrcName = msg.src_name.includes(":")
          ? sanitizeDID(msg.src_name)
          : msg.src_name;
        const sanitizedDesName = msg.des_name.includes(":")
          ? sanitizeDID(msg.des_name)
          : msg.des_name;

        participantDetails.set(sanitizedSrcName, sanitizeDID(msg.src_did));
        participantDetails.set(sanitizedDesName, sanitizeDID(msg.des_did));
      });
    });
  });

  // Add participants to the mermaid string with names and sanitized DIDs
  participantDetails.forEach((sanitizedDID, name) => {
    mermaidString += `    participant ${name} as ${name} <br/>${sanitizedDID}\n`;
  });

  // Iterate through each group
  data.forEach((item: any) => {
    let groupParticipants: any = new Set(); // This will collect participants for the current group

    // Collect participants involved in each specific group
    Object.values(item.groups).forEach((group: any) => {
      group.forEach((msg: any) => {
        const sanitizedSrcName = msg.src_name.includes(":")
          ? sanitizeDID(msg.src_name)
          : msg.src_name;
        const sanitizedDesName = msg.des_name.includes(":")
          ? sanitizeDID(msg.des_name)
          : msg.des_name;

        groupParticipants.add(sanitizedSrcName);
        groupParticipants.add(sanitizedDesName);
      });
    });

    // Convert the set of participants to a sorted array and then to a string
    groupParticipants = Array.from(groupParticipants).sort().join(",");

    // Get the group color from the config
    const groupColor = getGroupColor(item.group_name);

    // Add group note with only involved participants
    mermaidString += `\n    rect ${groupColor}\n    Note over ${groupParticipants}: ${item.group_name}\n`;

    Object.entries(item.groups).forEach(([groupId, messages]: any) => {
      mermaidString += `    alt Group Id ${groupId}\n`;
      messages.forEach((msg: any) => {
        const sanitizedSrcName = msg.src_name.includes(":")
          ? sanitizeDID(msg.src_name)
          : msg.src_name;
        const sanitizedDesName = msg.des_name.includes(":")
          ? sanitizeDID(msg.des_name)
          : msg.des_name;
        const arrow = sanitizedSrcName > sanitizedDesName ? "-->>" : "->>";
        mermaidString += `    ${sanitizedSrcName}${arrow}${sanitizedDesName}: [${msg.msg_type_name}]: Event Message ${msg.id}\n`;
      });
      mermaidString += "    end\n";
    });
    mermaidString += "    end\n";
  });

  return mermaidString;
};

export function extractAllEventMessages(data: any) {
  const allMessagesArray: any = [];

  if (!data || data.length === 0) return allMessagesArray;
  else
    data.forEach((groupData: any) => {
      Object.values(groupData.groups).forEach((messages: any) => {
        messages.forEach((message: any) => {
          allMessagesArray.push(message);
        });
      });
    });
  return allMessagesArray;
}
