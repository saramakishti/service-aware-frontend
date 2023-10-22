import { AxiosError } from "axios";
import React, {
  createContext,
  Dispatch,
  ReactNode,
  SetStateAction,
  useState,
} from "react";

type AppContextType = {
  data: AppState;

  isLoading: boolean;
  error: AxiosError<any> | undefined;

  setAppState: Dispatch<SetStateAction<AppState>>;
};

export const AppContext = createContext<AppContextType>({} as AppContextType);

type AppState = NonNullable<unknown>;

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
