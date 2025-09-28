// frontend/components/JobCard.js
export default function JobCard({ title, company, location, url }) {
  return (
    <div className="bg-white p-6 rounded-xl shadow-lg hover:shadow-2xl transition-all duration-300 transform hover:-translate-y-1 w-full">
      <h2 className="text-xl font-semibold text-gray-900">{title}</h2>
      <p className="text-gray-700 mt-1">{company} — {location}</p>
      <a
        href={url}
        target="_blank"
        rel="noopener noreferrer"
        className="mt-4 inline-block text-blue-600 font-medium hover:underline"
      >
        Apply
      </a>
    </div>
  );
}
