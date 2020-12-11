const _ = require(`lodash`)

require("dotenv").config({
  path: `.env.${process.env.NODE_ENV}`,
})

module.exports = {
  pathPrefix: process.env.PATH_PREFIX,
  siteMetadata: {
    lang: `ja`,
    title: `プログラミング言語別単価チャート`,
    description: `プログラミング言語別に単価を集計＆グラフ化したサイトです。`,
    author: `@okdyy75`,
  },
  plugins: [
    `gatsby-plugin-react-helmet`,
    {
      resolve: `gatsby-source-filesystem`,
      options: {
        name: `images`,
        path: `${__dirname}/src/images`,
      },
    },
    {
      resolve: `gatsby-source-filesystem`,
      options: {
        name: `levtech`,
        path: `../data/levtech/`,
      },
    },
    {
      resolve: `gatsby-transformer-csv`,
      options: {
        typeName: ({ node }) =>
          _.upperFirst(_.camelCase(`${node.sourceInstanceName} ${node.relativeDirectory} ${node.extension}`)),
      },
    },
    `gatsby-transformer-sharp`,
    `gatsby-plugin-sharp`,
    {
      resolve: `gatsby-plugin-manifest`,
      options: {
        name: `GatsbyJS`,
        short_name: `GatsbyJS`,
        start_url: `/`,
        background_color: `#f7f0eb`,
        theme_color: `#a2466c`,
        display: `standalone`,
        icon: `src/images/gatsby-icon.png`,
      },
    },
    // this (optional) plugin enables Progressive Web App + Offline functionality
    // To learn more, visit: https://gatsby.dev/offline
    // `gatsby-plugin-offline`,
    "gatsby-plugin-theme-ui",
  ],
}
