import { useContext } from "react";
import { AppContext } from "./useAppContext";

const useGetEntityByName = (nameOrDid: string) => {
  const { data } = useContext(AppContext);
  const allEntities = data.allEntities;

  if (!allEntities) {
    return { entity: undefined, isLoading: true };
  }

  const entity = allEntities.find(
    (entity) => entity.name === nameOrDid || entity.did === nameOrDid,
  );

  return { entity, isLoading: false };
};

export default useGetEntityByName;
