# Activity Photos

This gallery dynamically loads all images from the current folder.

<style>
  .gallery {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 10px;
  }
  .gallery img {
    width: 100%;
    height: auto;
    border-radius: 5px;
  }
</style>

<div class="gallery" id="imageGallery">Loading images...</div>

<script>
  // Since index.md, images, and gallery.json are in the same folder, we leave out any folder prefix.
  const jsonFile = 'images.json'; // JSON file with image names

  fetch(jsonFile)
    .then(response => response.json())
    .then(images => {
      const gallery = document.getElementById('imageGallery');
      gallery.innerHTML = ''; // Remove the loading text

      images.forEach(imageName => {
        let img = document.createElement('img');
        img.src = imageName;  // Directly use the image name (e.g., "image1.jpg")
        img.alt = imageName;
        gallery.appendChild(img);
      });
    })
    .catch(error => console.error('Error loading images:', error));
</script>
