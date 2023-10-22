import Image from "next/image";
import {
  default as clanDark,
  default as clanLight,
} from "../../public/clan-dark.png";
import { useAppState } from "./hooks/useAppContext";

export default function Background() {
  const { isLoading } = useAppState();

  return (
    <div
      className={
        "fixed -z-10 h-[100vh] w-[100vw] overflow-hidden opacity-10 blur-md dark:opacity-40"
      }
    >
      {isLoading && (
        <>
          <Image
            className="dark:hidden"
            alt="clan"
            src={clanLight}
            placeholder="blur"
            quality={100}
            fill
            sizes="100vw"
            style={{
              objectFit: "cover",
            }}
          />
          <Image
            className="hidden dark:block"
            alt="clan"
            src={clanDark}
            placeholder="blur"
            quality={100}
            fill
            sizes="100vw"
            style={{
              objectFit: "cover",
            }}
          />
        </>
      )}
    </div>
  );
}
