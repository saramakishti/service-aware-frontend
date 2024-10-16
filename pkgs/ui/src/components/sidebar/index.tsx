import {
  Divider,
  IconButton,
  List,
  ListItem,
  ListItemButton,
  ListItemIcon,
  ListItemText,
  Tooltip,
  useMediaQuery,
} from "@mui/material";
import { useGetEntityByRole } from "@/api/entities/entities";
import { Role } from "@/api/model/role";
import Image from "next/image";
import React, { ReactNode } from "react";

import { tw } from "@/utils/tailwind";
import Collapse from "@mui/material/Collapse";
import Link from "next/link";
import ChevronLeftIcon from "@mui/icons-material/ChevronLeft";
import HomeIcon from "@mui/icons-material/Home";
import HubIcon from "@mui/icons-material/Hub";
import PersonIcon from "@mui/icons-material/Person";
import RouterIcon from "@mui/icons-material/Router";
import StorageIcon from "@mui/icons-material/Storage";
import ExpandLess from "@mui/icons-material/ExpandLess";
import ExpandMore from "@mui/icons-material/ExpandMore";

type MenuEntry = {
  icon: ReactNode;
  label: string;
  to: string;
  disabled: boolean;
} & {
  subMenuEntries?: MenuEntry[];
};

export const menuEntries: MenuEntry[] = [
  {
    icon: <HomeIcon />,
    label: "Home",
    to: "/",
    disabled: false,
  },
  {
    icon: <HubIcon />,
    label: "Entities",
    to: "/entities",
    disabled: false,
  },
  {
    icon: <RouterIcon />,
    label: "AP",
    to: "/access-point",
    disabled: false,
  },
  {
    icon: <StorageIcon />,
    label: "DLG",
    to: "/distributed-ledger-gateway",
    disabled: false,
  },
];

const hideSidebar = tw`-translate-x-14 lg:-translate-x-64`;
const showSidebar = tw`lg:translate-x-0`;

interface SidebarProps {
  show: boolean;
  onClose: () => void;
}

export function Sidebar(props: SidebarProps) {
  const { data: entityData } = useGetEntityByRole({
    role: Role.service_prosumer,
  });
  const { show, onClose } = props;
  const [activeMenuItem, setActiveMenuItem] = React.useState(
    typeof window !== "undefined" ? window.location.pathname : "",
  );
  const [collapseMenuOpen, setCollapseMenuOpen] = React.useState(true);

  const isSmallerScreen = useMediaQuery("(max-width: 1025px)");

  const handleMenuItemClick = (path: string) => {
    setActiveMenuItem(path);
  };

  const handleCollapseClick = () => {
    setCollapseMenuOpen(!collapseMenuOpen);
  };

  const menuEntityEntries: MenuEntry[] = React.useMemo(() => {
    if (entityData) {
      return Array.isArray(entityData.data)
        ? entityData.data.map((entity: any) => ({
            icon: <PersonIcon />,
            label: entity.name,
            to: entity.name,
            disabled: false,
          }))
        : [];
    } else {
      return [];
    }
  }, [entityData]);

  React.useEffect(() => {
    if (isSmallerScreen) {
      setCollapseMenuOpen(false);
    } else {
      setCollapseMenuOpen(true);
    }
  }, [isSmallerScreen, entityData]);

  return (
    <aside
      style={{ backgroundColor: "#00497c" }}
      className={tw`${
        show ? showSidebar : hideSidebar
      } z-9999 static left-0  top-0 flex h-screen w-14 flex-col overflow-x-hidden overflow-y-hidden bg-neutral-10 transition duration-150 ease-in-out dark:bg-neutral-2 lg:w-64`}
    >
      <div className="flex items-center justify-between gap-2 overflow-hidden px-0 py-5 lg:p-6">
        <div className="mt-8 hidden w-full text-center font-semibold text-white lg:block">
          <Image
            src="/tub-logo.png"
            alt="TU Berlin Logo"
            width={125}
            height={90}
            priority
          />
        </div>
        <div className="lg:absolute lg:right-0 lg:top-0">
          <Tooltip
            placement="right"
            title={collapseMenuOpen ? "Close Sidebar" : "Expand Sidebar"}
          >
            <IconButton size="large" className="text-white" onClick={onClose}>
              <ChevronLeftIcon fontSize="inherit" />
            </IconButton>
          </Tooltip>
        </div>
      </div>
      <Divider
        flexItem
        className="mx-8 mb-4 mt-9 hidden bg-neutral-40 lg:block"
      />
      <div className="flex flex-col overflow-hidden overflow-y-auto">
        <List className="mb-14 px-0 pb-4 text-white lg:mt-1 lg:px-4">
          {menuEntries.map((menuEntry, idx) => {
            return (
              <ListItem
                key={idx}
                disablePadding
                className="!overflow-hidden py-2"
              >
                {menuEntry.label !== "Entities" ? (
                  <ListItemButton
                    className="justify-center lg:justify-normal"
                    LinkComponent={Link}
                    href={menuEntry.to}
                    disabled={menuEntry.disabled}
                    selected={activeMenuItem === menuEntry.to}
                    onClick={() => handleMenuItemClick(menuEntry.to)}
                  >
                    <ListItemIcon
                      color="inherit"
                      className="justify-center overflow-hidden text-white lg:justify-normal"
                    >
                      {menuEntry.icon}
                    </ListItemIcon>
                    <ListItemText
                      primary={menuEntry.label}
                      primaryTypographyProps={{
                        color: "inherit",
                      }}
                      className="hidden lg:block"
                    />
                  </ListItemButton>
                ) : (
                  <div>
                    <ListItemButton
                      className="justify-center lg:justify-normal"
                      disabled={menuEntry.disabled}
                      selected={activeMenuItem === menuEntry.to}
                      onClick={handleCollapseClick}
                    >
                      <ListItemIcon
                        color="inherit"
                        className="overflow-hidden text-white lg:justify-normal"
                      >
                        {menuEntry.icon}
                      </ListItemIcon>
                      <ListItemText
                        primary={menuEntry.label}
                        primaryTypographyProps={{
                          color: "inherit",
                        }}
                        className="mr-4 hidden lg:block"
                      />
                      {collapseMenuOpen ? <ExpandLess /> : <ExpandMore />}
                    </ListItemButton>
                    <Collapse
                      in={collapseMenuOpen && show}
                      timeout="auto"
                      unmountOnExit
                    >
                      <List component="div" disablePadding>
                        {menuEntityEntries?.map((menuEntry, idx) => (
                          <Link
                            key={"entity-link-" + idx}
                            href={`/client?name=${menuEntry.to}`}
                            style={{ textDecoration: "none", color: "white" }}
                          >
                            <ListItemButton
                              key={idx}
                              sx={{ pl: 4 }}
                              className="lg:justify-normal"
                              LinkComponent={Link}
                              disabled={menuEntry.disabled}
                              selected={activeMenuItem === menuEntry.to}
                              onClick={() => handleMenuItemClick(menuEntry.to)}
                            >
                              <ListItemIcon
                                color="inherit"
                                className="overflow-hidden text-white lg:justify-normal"
                              >
                                {menuEntry.icon}
                              </ListItemIcon>
                              <ListItemText
                                primary={menuEntry.label}
                                primaryTypographyProps={{
                                  color: "inherit",
                                }}
                                className="hidden lg:block"
                              />
                            </ListItemButton>
                          </Link>
                        ))}
                      </List>
                    </Collapse>
                  </div>
                )}
              </ListItem>
            );
          })}
        </List>
      </div>
    </aside>
  );
}
