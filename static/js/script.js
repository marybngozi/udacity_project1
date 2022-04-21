window.parseISOString = function parseISOString(s) {
  var b = s.split(/\D+/);
  return new Date(Date.UTC(b[0], --b[1], b[2], b[3], b[4], b[5], b[6]));
};

// delete a venue
document.querySelector("#delete_venue").addEventListener("click", (e) => {
  const venueId = e.target.dataset["id"];

  // verify if the delete was intentional
  if (
    !confirm(
      "Are you sure you want to delete this Venue and its associated Shows?"
    )
  ) {
    return;
  }

  fetch(`/venues/${venueId}`, {
    method: "DELETE",
  })
    .then((res) => {
      console.log(res);
      // go to the homepage
      window.location = "/";
    })
    .catch((err) => {
      console.log({ err });
    });
});
