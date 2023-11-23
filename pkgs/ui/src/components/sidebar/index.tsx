import {
    Divider,
    IconButton,
    List,
    ListItem,
    ListItemButton,
    ListItemIcon,
    ListItemText,
} from "@mui/material";
import Image from "next/image";
import React, {ReactNode} from "react";

import {tw} from "@/utils/tailwind";
import Collapse from '@mui/material/Collapse';
import Link from "next/link";
import ChevronLeftIcon from "@mui/icons-material/ChevronLeft";
import HomeIcon from "@mui/icons-material/Home";
import HubIcon from "@mui/icons-material/Hub";
import PersonIcon from "@mui/icons-material/Person";
import RouterIcon from "@mui/icons-material/Router";
import StorageIcon from "@mui/icons-material/Storage";
import ExpandLess from '@mui/icons-material/ExpandLess';
import ExpandMore from '@mui/icons-material/ExpandMore';

type MenuEntry = {
    icon: ReactNode;
    label: string;
    to: string;
    disabled: boolean;
} & {
    subMenuEntries?: MenuEntry[];
};

const menuEntityEntries: MenuEntry[] = [
    {
        icon: <PersonIcon/>,
        label: "C1",
        to: "/client-1",
        disabled: false,
    },
    {
        icon: <PersonIcon/>,
        label: "C2",
        to: "/client-2",
        disabled: false,
    }
];

const menuEntries: MenuEntry[] = [
    {
        icon: <HomeIcon/>,
        label: "Home",
        to: "/",
        disabled: false,
    },
    {
        icon: <HubIcon/>,
        label: "Entities",
        to: "/entities",
        disabled: false,
    },
    {
        icon: <RouterIcon/>,
        label: "AP",
        to: "/access-point",
        disabled: false,
    },
    {
        icon: <StorageIcon/>,
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
    const {show, onClose} = props;
    const [activeMenuItem, setActiveMenuItem] = React.useState(typeof window !== "undefined" ? window.location.pathname : "");
    const [collapseMenuOpen, setCollapseMenuOpen] = React.useState(true);

    const handleCollapseClick = () => {
        setCollapseMenuOpen(!collapseMenuOpen);
    };

    const handleMenuItemClick = (path: string) => {
        setActiveMenuItem(path);
    };

    return (
        <aside
            style={{backgroundColor: "#00497c"}}
            className={tw`${
                show ? showSidebar : hideSidebar
            } z-9999 static left-0  top-0 flex h-screen w-14 flex-col overflow-x-hidden overflow-y-hidden bg-neutral-10 transition duration-150 ease-in-out dark:bg-neutral-2 lg:w-64`}
        >
            <div className="flex items-center justify-between gap-2 overflow-hidden px-0 py-5 lg:p-6">
                <div className="mt-8 hidden w-full text-center font-semibold text-white lg:block">
                    <Image
                        src="/logo.png"
                        alt="TUB Logo"
                        width={75}
                        height={75}
                        priority
                    />
                </div>
            </div>
            <Divider
                flexItem
                className="mx-8 mb-4 mt-9 hidden bg-neutral-40 lg:block"
            />
            <div className="flex w-full justify-center">
                <IconButton size="large" className="text-white" onClick={onClose}>
                    <ChevronLeftIcon fontSize="inherit"/>
                </IconButton>
            </div>
            <div className="flex flex-col overflow-hidden overflow-y-auto">
                <List className="mb-14 px-0 pb-4 text-white lg:mt-1 lg:px-4">
                    {menuEntries.map((menuEntry, idx) => {
                        return (
                            <ListItem
                                key={idx}
                                disablePadding
                                className="!overflow-hidden py-2"
                            >
                                {menuEntry.label !== "Entities" ?
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
                                    :
                                    <div>
                                        <ListItemButton
                                            className="justify-center lg:justify-normal"
                                            disabled={menuEntry.disabled}
                                            selected={activeMenuItem === menuEntry.to}
                                            onClick={handleCollapseClick}>
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
                                            {collapseMenuOpen ? <ExpandLess/> : <ExpandMore/>}
                                        </ListItemButton>
                                        <Collapse in={collapseMenuOpen} timeout="auto" unmountOnExit>
                                            <List component="div" disablePadding>
                                                {menuEntityEntries.map((menuEntry, idx) => (
                                                    <ListItemButton key={idx} sx={{pl: 4}}
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
                                                ))}
                                            </List>
                                        </Collapse>
                                    </div>
                                }
                            </ListItem>
                        );
                    })}
                </List>
            </div>
        </aside>
    );
}
