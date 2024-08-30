import globals from "globals";
import pluginJs from "@eslint/js";
import tseslint from "typescript-eslint";
import pluginReact from "eslint-plugin-react";
import pluginNext from "@next/eslint-plugin-next";
import pluginHooks from "eslint-plugin-react-hooks"


export default [
  {files: ["**/*.{js,mjs,cjs,ts,jsx,tsx}"]},
  {languageOptions: { globals: globals.browser },},
  pluginJs.configs.recommended,
  ...tseslint.configs.recommended,
  ...pluginReact.configs.flat.recommended,
  ...pluginHooks.configs.recommended,
  ...pluginNext.configs.recommended,
];