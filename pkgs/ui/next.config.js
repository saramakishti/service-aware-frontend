/** @type {import('next').NextConfig} */
const nextConfig = {
  output: "export",
  images: { unoptimized: true },
  eslint: {
    dirs: ["src"],
  },
  generateBuildId: async () => {
    // This could be anything, using the latest git hash
    return process.env.NEXT_BUILD_ID;
  },
  outputFileTracing: true,
  reactStrictMode: true,
};

module.exports = nextConfig;
