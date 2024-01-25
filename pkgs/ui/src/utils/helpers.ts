import { projectConfig } from "@/config/config";

export const formatDateTime = (date: string | number) => {
  const dateToFormat = typeof date === "number" ? date * 1000 : date;
  const _date = new Date(dateToFormat);
  return _date.toLocaleDateString("en-US", {
    year: "numeric",
    month: "long",
    day: "numeric",
    hour: "2-digit",
    minute: "2-digit",
    second: "2-digit",
    hour12: true,
  });
};

export function sanitizeDID(did: string) {
  return did.replace(/:/g, "_");
}

export function getGroupColor(groupName: string) {
  const group = projectConfig.GROUPS.find(
    (g: any) => g.groupName === groupName,
  );
  return group ? group.groupColor : "rgb(211, 211, 211)"; // Light gray if not found
}

export function getGroupById(groupId: string | number) {
  const group = projectConfig.GROUPS.find((g: any) => g.groupId === groupId);
  return group ? group : {};
}
