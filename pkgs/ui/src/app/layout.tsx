"use client";
import { Sidebar } from "@/components/sidebar";
import { tw } from "@/utils/tailwind";
import MenuIcon from "@mui/icons-material/Menu";
import {
  CssBaseline,
  IconButton,
  ThemeProvider,
  useMediaQuery,
} from "@mui/material";
import { StyledEngineProvider } from "@mui/material/styles";
import axios from "axios";
import localFont from "next/font/local";
import * as React from "react";
import { Toaster } from "react-hot-toast";
import "./globals.css";
import { darkTheme, lightTheme } from "./theme/themes";

import Background from "@/components/background";
import { AppContext, WithAppState } from "@/components/hooks/useAppContext";

const roboto = localFont({
  src: [
    {
      path: "../fonts/truetype/Roboto-Regular.ttf",
      weight: "400",
      style: "normal",
    },
  ],
});

axios.defaults.baseURL = "http://localhost:2979";

// add negative margin for smooth transition to fill the space of the sidebar
const translate = tw`lg:-ml-64 -ml-14`;

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  const userPrefersDarkmode = useMediaQuery("(prefers-color-scheme: dark)");

  const [showSidebar, setShowSidebar] = React.useState(true);

  return (
    <html lang="en">
      <head>
        <title>Service Aware Networks</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <meta name="description" content="Service Aware Networks" />
        <link rel="icon" href="tub-favicon.ico" sizes="any" />
        <script type="module">
          import mermaid from
          'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
        </script>
        <script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
        <script
          // eslint-disable-next-line react/no-danger
          dangerouslySetInnerHTML={{
            __html: `mermaid.initialize({startOnLoad: true});`,
          }}
        />
      </head>
      <StyledEngineProvider injectFirst>
        <ThemeProvider theme={userPrefersDarkmode ? darkTheme : lightTheme}>
          <body id="__next" className={roboto.className}>
            <CssBaseline />
            <Toaster />
            <WithAppState>
              <AppContext.Consumer>
                {(appState) => {
                  const showSidebarDerived = Boolean(
                    showSidebar && !appState.isLoading,
                  );
                  return (
                    <>
                      <Background />
                      <div className="flex h-screen overflow-hidden">
                        <Sidebar
                          show={showSidebarDerived}
                          onClose={() => setShowSidebar(false)}
                        />
                        <div
                          className={tw`${
                            !showSidebarDerived && translate
                          } flex h-full w-full flex-col overflow-y-scroll transition-[margin] duration-150 ease-in-out`}
                        >
                          <div className="grid grid-cols-3">
                            <div className="col-span-1">
                              <IconButton
                                style={{ padding: "12px" }}
                                hidden={true}
                                onClick={() => setShowSidebar((c) => !c)}
                              >
                                {!showSidebar && <MenuIcon />}
                              </IconButton>
                            </div>
                          </div>

                          <div className="px-1">
                            <div className="relative flex h-full flex-1 flex-col">
                              <main>{children}</main>
                            </div>
                          </div>
                        </div>
                      </div>
                    </>
                  );
                }}
              </AppContext.Consumer>
            </WithAppState>
          </body>
        </ThemeProvider>
      </StyledEngineProvider>
    </html>
  );
}
