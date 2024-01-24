import AttachmentIcon from "@mui/icons-material/Attachment";
import ArticleIcon from "@mui/icons-material/Article";
import ConstructionIcon from "@mui/icons-material/Construction";
import AssignmentTurnedInIcon from "@mui/icons-material/AssignmentTurnedIn";
import RemoveCircleIcon from "@mui/icons-material/RemoveCircle";
import AddCircleIcon from "@mui/icons-material/AddCircle";
import PageviewIcon from "@mui/icons-material/Pageview";
import BuildIcon from "@mui/icons-material/Build";

// Palette: https://coolors.co/palette/ff9aa2-feb7b1-ffdac0-ffecc4-e2f0cc-b5ead6-b7dbeb-c7ceea

export const projectConfig = {
  BASE_URL: "http://localhost:2979/api/v1",
  GROUPS: {
    1: {
      groupName: "Attachment",
      groupColor: "rgb(255, 154, 162)",
      groupIcon: AttachmentIcon,
      messageTypes: [
        { id: 1, label: "Attachment Request Send" },
        { id: 2, label: "Attachment Request Received" },
        { id: 3, label: "Attachment Response Send" },
        { id: 4, label: "Attachment Response Received" },
      ],
    },
    2: {
      groupName: "Connection Setup",
      groupColor: "rgb(254, 183, 177)",
      groupIcon: ConstructionIcon,
      messageTypes: [
        { id: 1, label: "Connection request send" },
        { id: 2, label: "Connection request received" },
        { id: 3, label: "Connection response send" },
        { id: 4, label: "Connection response received" },
      ],
    },
    3: {
      groupName: "Presentation",
      groupColor: "rgb(255, 218, 192)",
      groupIcon: ArticleIcon,
      messageTypes: [
        { id: 1, label: "Request send" },
        { id: 2, label: "Request received" },
        { id: 3, label: "Presentation send" },
        { id: 4, label: "Presentation received" },
        { id: 5, label: "Presentation acknowledged" },
      ],
    },
    4: {
      groupName: "DID Resolution",
      groupColor: "rgb(255, 236, 196)",
      groupIcon: AssignmentTurnedInIcon,
      messageTypes: [
        { id: 1, label: "DID Resolution Request send" },
        { id: 2, label: "DID Resolution Request received" },
        { id: 3, label: "DID Resolution Response send" },
        { id: 4, label: "DID Resolution Response received" },
      ],
    },
    5: {
      groupName: "Service De-registration",
      groupColor: "rgb(226, 240, 204)",
      groupIcon: RemoveCircleIcon,
      messageTypes: [
        { id: 1, label: "Service De-registration send" },
        { id: 2, label: "Service De-registration received" },
        { id: 3, label: "Service De-registration successful send" },
        { id: 4, label: "Service De-registration successful received" },
      ],
    },
    6: {
      groupName: "Service Registration",
      groupColor: "rgb(181, 234, 214)",
      groupIcon: AddCircleIcon,
      messageTypes: [
        { id: 1, label: "Service Registration send" },
        { id: 2, label: "Service Registration received" },
        { id: 3, label: "Service Registration successful send" },
        { id: 4, label: "Service Registration successful received" },
      ],
    },
    7: {
      groupName: "Service Discovery",
      groupColor: "rgb(183, 219, 235)",
      groupIcon: PageviewIcon,
      messageTypes: [
        { id: 1, label: "Service Discovery send" },
        { id: 2, label: "Service Discovery received" },
        { id: 3, label: "Service Discovery Result send" },
        { id: 4, label: "Service Discovery Result received" },
      ],
    },
    8: {
      groupName: "Service Operation",
      groupColor: "rgb(199, 206, 234)",
      groupIcon: BuildIcon,
      messageTypes: [
        { id: 1, label: "Service Request Send" },
        { id: 2, label: "Service Request Received" },
        { id: 3, label: "Service Response Send" },
        { id: 4, label: "Service Response Received" },
      ],
    },
  },
};

export const iconMatch: any = {
  Attachement: <AttachmentIcon />,
  Presentation: <ArticleIcon />,
  "DID Resolution": <AssignmentTurnedInIcon />,
  "Connection Setup": <ConstructionIcon />,
};
