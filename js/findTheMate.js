var str =
  "Sometimes (when I nest them (my parentheticals) too much (like this (and this))) they get confusing.";

findTheMate(str, "(", ")", 10);

/**
 * Find the mate of a given character
 * @param {str}    sentence      The string we want to search in
 * @param {str}    character     What we want to match
 * @param {str}    mate          What we want to match against
 * @param {int}    place         The place of the character to start with
 *
 */
function findTheMate(sentence, character, mate, place) {
  var i = 0,
    len = sentence.length,
    search = "";

  for (len; place < len; place++) {
    search += sentence[place];
    if (sentence[place] === character) {
      i++;
    } else if (sentence[place] === mate) {
      i--;
    }

    if (i === 0) {
      console.log(place);
      // console.log(search);
      return;
    }
  }
}
