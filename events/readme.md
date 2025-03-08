# Events Photos

<style>
  .gallery {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
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
  const jsonFile = 'images.json'; // JSON file with image names

  fetch(jsonFile)
    .then(response => {
      if (!response.ok) {
        throw new Error('Network response was not ok ' + response.statusText);
      }
      return response.json();
    })
    .then(images => {
      const gallery = document.getElementById('imageGallery');
      gallery.innerHTML = ''; // Remove the loading text

      images.forEach(imageName => {
        let img = document.createElement('img');
        img.src = imageName;  // Ensure this path is correct relative to index.md
        img.alt = imageName;
        gallery.appendChild(img);
      });
    })
    .catch(error => console.error('Error loading images:', error));
</script>
