import { useListMachines } from "@/api/default/default";
import { MachinesResponse } from "@/api/model";
import { AxiosError, AxiosResponse } from "axios";
import React, {
  createContext,
  Dispatch,
  ReactNode,
  SetStateAction,
  useState,
} from "react";
import { KeyedMutator } from "swr";

type AppContextType = {
  data: AppState;

  isLoading: boolean;
  error: AxiosError<any> | undefined;

  setAppState: Dispatch<SetStateAction<AppState>>;
};

export const AppContext = createContext<AppContextType>({} as AppContextType);

type AppState = {};

interface AppContextProviderProps {
  children: ReactNode;
}
export const WithAppState = (props: AppContextProviderProps) => {
  const { children } = props;

  const isLoading = false;
  const error = undefined;

  const [data, setAppState] = useState<AppState>({});

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
