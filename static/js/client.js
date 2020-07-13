var GRAY_ICON = 'https://i.ibb.co/2N1pb2y/inspiration.png';

window.TrelloPowerUp.initialize({
  'card-back-section': function(t, options){
    return {
      title: 'Random Inspiration',
      icon: GRAY_ICON,
      content: {
        type: 'iframe',
        url: t.signUrl("/section.html"),
        height: 10
      }
    };
  }
});