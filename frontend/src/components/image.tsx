import React from "react"
import { useStaticQuery, graphql } from "gatsby"
import Img from "gatsby-image"
const _ = require("lodash")

/*
 * This component is built using `gatsby-image` to automatically serve optimized
 * images with lazy loading and reduced file sizes. The image is loaded using a
 * `useStaticQuery`, which allows us to load the image from directly within this
 * component, rather than having to pass the image data down from pages.
 *
 * For more information, see the docs:
 * - `gatsby-image`: https://gatsby.dev/gatsby-image
 * - `useStaticQuery`: https://www.gatsbyjs.com/docs/use-static-query/
 */

type Props = {
  path: string
  width: Number | string
  height: Number | string
}

const Image = ({ path, width, height }: Props) => {
  const data = useStaticQuery(graphql`
    {
      gatsbyIcon: file(relativePath: { eq: "gatsby-icon.png" }) {
        childImageSharp {
          fluid(maxWidth: 300) {
            ...GatsbyImageSharpFluid
          }
        }
      }
      notFound: file(relativePath: { eq: "not-found.png" }) {
        childImageSharp {
          fluid(maxWidth: 300) {
            ...GatsbyImageSharpFluid
          }
        }
      }
    }
  `)
  const images = [data.gatsbyIcon.childImageSharp, data.notFound.childImageSharp]
  const image = _.find(images, (v, k) => v.fluid.src.indexOf(path) !== -1)
  if (!image) {
    return <div>Picture not found</div>
  }

  return <Img fluid={image.fluid} fadeIn={false} style={{ width: width, height: height }} />
}

export default Image
