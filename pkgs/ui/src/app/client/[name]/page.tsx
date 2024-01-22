import Client from "@/app/client/client";
import { menuEntityEntries } from "@/components/sidebar";

export const dynamic = "error";
export const dynamicParams = false;
/*
The generateStaticParams function can be used in combination with dynamic route segments
to statically generate routes at build time instead of on-demand at request time.
During next dev, generateStaticParams will be called when you navigate to a route.
During next build, generateStaticParams runs before the corresponding Layouts or Pages are generated.
https://nextjs.org/docs/app/api-reference/functions/generate-static-params
*/
export function generateStaticParams() {
  return menuEntityEntries.map((entry) => ({
    name: entry.label,
  }));
}

export default function Page({ params }: { params: { name: string } }) {
  return <Client params={params} />;
}
