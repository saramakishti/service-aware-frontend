import AttachmentIcon from "@mui/icons-material/Attachment";
import ArticleIcon from "@mui/icons-material/Article";
import ConstructionIcon from "@mui/icons-material/Construction";
import AssignmentTurnedInIcon from "@mui/icons-material/AssignmentTurnedIn";
import RemoveCircleIcon from "@mui/icons-material/RemoveCircle";
import AddCircleIcon from "@mui/icons-material/AddCircle";
import PageviewIcon from "@mui/icons-material/Pageview";
import BuildIcon from "@mui/icons-material/Build";

export const projectConfig: any = {
  BASE_URL: "http://localhost:2979/api/v1",
  REFRESH_FREQUENCY: 2000,
  GROUPS: [
    {
      groupName: "Attachement",
      groupId: 1,
      groupColor: "rgb(230, 230, 250)",
      groupIcon: <AttachmentIcon />,
      messageTypes: [
        { id: 1, label: "Attachment Request Send" },
        { id: 2, label: "Attachment Request Received" },
        { id: 3, label: "Attachment Response Send" },
        { id: 4, label: "Attachment Response Received" },
      ],
    },
    {
      groupName: "Connection Setup",
      groupId: 2,
      groupColor: "rgb(245, 222, 179)",
      groupIcon: <ConstructionIcon />,
      messageTypes: [
        { id: 1, label: "Connection request send" },
        { id: 2, label: "Connection request received" },
        { id: 3, label: "Connection response send" },
        { id: 4, label: "Connection response received" },
      ],
    },
    {
      groupName: "Presentation",
      groupId: 3,
      groupColor: "rgb(255, 209, 220)",
      groupIcon: <ArticleIcon />,
      messageTypes: [
        { id: 1, label: "Request send" },
        { id: 2, label: "Request received" },
        { id: 3, label: "Presentation send" },
        { id: 4, label: "Presentation received" },
        { id: 5, label: "Presentation acknowledged" },
      ],
    },
    {
      groupName: "DID Resolution",
      groupId: 4,
      groupColor: "rgb(189, 255, 243)",
      groupIcon: <AssignmentTurnedInIcon />,
      messageTypes: [
        { id: 1, label: "DID Resolution Request send" },
        { id: 2, label: "DID Resolution Request received" },
        { id: 3, label: "DID Resolution Response send" },
        { id: 4, label: "DID Resolution Response received" },
      ],
    },
    {
      groupName: "Service De-registration",
      groupId: 5,
      groupColor: "rgb(255, 218, 185)",
      groupIcon: <RemoveCircleIcon />,
      messageTypes: [
        { id: 1, label: "Service De-registration send" },
        { id: 2, label: "Service De-registration received" },
        { id: 3, label: "Service De-registration successful send" },
        { id: 4, label: "Service De-registration successful received" },
      ],
    },
    {
      groupName: "Service Registration",
      groupId: 6,
      groupColor: "rgb(200, 162, 200)",
      groupIcon: <AddCircleIcon />,
      messageTypes: [
        { id: 1, label: "Service Registration send" },
        { id: 2, label: "Service Registration received" },
        { id: 3, label: "Service Registration successful send" },
        { id: 4, label: "Service Registration successful received" },
      ],
    },
    {
      groupName: "Service Discovery",
      groupId: 7,
      groupColor: "rgb(255, 250, 205)",
      groupIcon: <PageviewIcon />,
      messageTypes: [
        { id: 1, label: "Service Discovery send" },
        { id: 2, label: "Service Discovery received" },
        { id: 3, label: "Service Discovery Result send" },
        { id: 4, label: "Service Discovery Result received" },
      ],
    },
    {
      groupName: "Service Operation",
      groupId: 8,
      groupColor: "rgb(135, 206, 235)",
      groupIcon: <BuildIcon />,
      messageTypes: [
        { id: 1, label: "Service Request Send" },
        { id: 2, label: "Service Request Received" },
        { id: 3, label: "Service Response Send" },
        { id: 4, label: "Service Response Received" },
      ],
    },
  ],
};
