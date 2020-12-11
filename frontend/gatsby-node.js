/**
 * Implement Gatsby's Node APIs in this file.
 *
 * See: https://www.gatsbyjs.com/docs/node-apis/
 */

// You can delete this file if you're not using it
const path = require(`path`)

exports.createPages = async ({ actions }) => {
  const { createPage } = actions

  createPage({
    path: `/levtech`,
    component: path.resolve(`./src/templates/site.tsx`),
    context: { site: `Levtech` },
  })
}
