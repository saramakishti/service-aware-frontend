import { useGetEntities } from "@/api/entities/entities";
import { Entity } from "@/api/model";
import { AxiosError } from "axios";
import React, {
  createContext,
  Dispatch,
  ReactNode,
  SetStateAction,
  useState,
  useEffect,
} from "react";

type AppContextType = {
  data: AppState;

  isLoading: boolean;
  error: AxiosError<any> | undefined;

  setAppState: Dispatch<SetStateAction<AppState>>;
};

export const AppContext = createContext<AppContextType>({} as AppContextType);

type AppState = {
  allEntities: Entity[] | undefined;
  loadingEntities: boolean;
  entitiesKeyFunc: any;
};

interface AppContextProviderProps {
  children: ReactNode;
}
export const WithAppState = (props: AppContextProviderProps) => {
  const { children } = props;

  const { data: entityData, swrKey: entitiesKeyFunc } = useGetEntities();

  const isLoading = false;
  const error = undefined;

  const [data, setAppState] = useState<AppState>({
    allEntities: [],
    loadingEntities: true,
    entitiesKeyFunc,
  });

  useEffect(() => {
    if (entityData) {
      setAppState((prevState) => ({
        ...prevState,
        allEntities: entityData.data,
        entitiesKeyFunc,
        loadingEntities: false,
      }));
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [entityData]);

  return (
    <AppContext.Provider
      value={{
        data,
        setAppState,
        isLoading,
        error,
      }}
    >
      {children}
    </AppContext.Provider>
  );
};

export const useAppState = () => React.useContext(AppContext);
