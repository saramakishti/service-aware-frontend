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
