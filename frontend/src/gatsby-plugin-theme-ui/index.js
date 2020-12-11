// https://github.com/system-ui/theme-ui/blob/master/packages/docs/src/gatsby-plugin-theme-ui/index.js
import { tosh } from "@theme-ui/presets"
export default {
  ...tosh,
  ...{
    colors: {
      text: "#000",
      background: "#fff",
      primary: "#07c",
      secondary: "#30c",
      muted: "#f6f6f6",
    },
    forms: {
      label: {
        fontFamily: `Silom, monospace`,
      },
      select: {
        fontFamily: `Silom, monospace`,
      },
    },
    text: {
      p: {
        padding: `2`,
        fontFamily: `Silom, monospace`,
      },
      h2: {
        mt: 2,
        mb: 3,
        borderBottom: `1px solid #ddd;`,
      },
      h3: {
        mt: 2,
        mb: 2,
      },
    },
    styles: {
      header: {
        display: `flex`,
        alignItems: `center`,
        maxWidth: 960,
        margin: `0 auto`,
        py: 4,
      },
      container: {
        maxWidth: 960,
        margin: `0 auto`,
        padding: 3,
      },
      footer: {
        display: "flex",
        flexWrap: "wrap",
        alignItems: "center",
        py: 4,
      },
      navlink: {
        fontFamily: `Silom, monospace`,
        display: `inline-block`,
        fontWeight: `bold`,
        color: `inherit`,
        textDecoration: `none`,
        ":hover,:focus": {
          color: `primary`,
        },
      },
    },
  },
}
